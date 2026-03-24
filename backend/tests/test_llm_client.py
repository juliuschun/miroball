"""MiroBall Backend - LLM client unit tests."""

import pytest
from unittest.mock import patch, MagicMock


def test_llm_client_init():
    """LLMClient initializes with default model."""
    from app.utils.llm_client import LLMClient
    with patch('app.utils.llm_client.anthropic.Anthropic'):
        client = LLMClient()
        assert client.model is not None


def test_llm_client_custom_model():
    """LLMClient accepts custom model name."""
    from app.utils.llm_client import LLMClient
    with patch('app.utils.llm_client.anthropic.Anthropic'):
        client = LLMClient(model='claude-sonnet-4-20250514')
        assert client.model == 'claude-sonnet-4-20250514'


def test_llm_client_chat_separates_system_message():
    """LLMClient.chat correctly separates system messages for Anthropic API."""
    from app.utils.llm_client import LLMClient

    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="test response")]

    with patch('app.utils.llm_client.anthropic.Anthropic') as mock_anthropic:
        mock_instance = MagicMock()
        mock_instance.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_instance

        client = LLMClient()
        result = client.chat([
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": "Hello"}
        ])

        call_kwargs = mock_instance.messages.create.call_args[1]
        assert call_kwargs["system"] == "You are helpful."
        assert len(call_kwargs["messages"]) == 1
        assert call_kwargs["messages"][0]["role"] == "user"
        assert result == "test response"


def test_llm_client_chat_json_cleans_markdown():
    """LLMClient.chat_json strips markdown code block wrappers."""
    from app.utils.llm_client import LLMClient

    mock_response = MagicMock()
    mock_response.content = [MagicMock(text='```json\n{"key": "value"}\n```')]

    with patch('app.utils.llm_client.anthropic.Anthropic') as mock_anthropic:
        mock_instance = MagicMock()
        mock_instance.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_instance

        client = LLMClient()
        result = client.chat_json([{"role": "user", "content": "Give JSON"}])

        assert result == {"key": "value"}
