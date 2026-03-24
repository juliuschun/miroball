"""
LLM客户端封装
Anthropic SDK 직접 호출 (Max subscription — API key 불필요)
"""

import json
import re
from typing import Optional, Dict, Any, List

import anthropic

from ..config import Config


class LLMClient:
    """LLM客户端 — Anthropic SDK 직접 호출"""

    def __init__(
        self,
        model: Optional[str] = None
    ):
        self.model = model or Config.LLM_MODEL_NAME
        # Max subscription: API key 없이 SDK 직접 사용
        self.client = anthropic.Anthropic()

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """发送聊天请求"""
        # system 메시지 분리 (Anthropic API 형식)
        system_msg = ""
        user_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system_msg = msg["content"]
            else:
                user_messages.append(msg)

        # JSON 모드 요청 시 system prompt에 지시 추가
        if response_format and response_format.get("type") == "json_object":
            json_instruction = "\n\nYou must respond with valid JSON only. No markdown, no explanation — just the JSON object."
            system_msg = (system_msg + json_instruction) if system_msg else json_instruction.strip()

        kwargs = {
            "model": self.model,
            "messages": user_messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if system_msg:
            kwargs["system"] = system_msg

        response = self.client.messages.create(**kwargs)
        content = response.content[0].text
        return content

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """发送聊天请求并返回JSON"""
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # 清理markdown代码块标记
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"LLM返回的JSON格式无效: {cleaned_response}")
