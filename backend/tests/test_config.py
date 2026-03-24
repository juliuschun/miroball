"""MiroBall Backend - Config tests."""

import os
import pytest


def test_config_loads():
    """Config class can be imported and instantiated."""
    from app.config import Config
    assert Config.MAX_CONTENT_LENGTH == 50 * 1024 * 1024
    assert Config.JSON_AS_ASCII is False


def test_config_default_model():
    """Default LLM model is set."""
    from app.config import Config
    assert Config.LLM_MODEL_NAME is not None
    assert len(Config.LLM_MODEL_NAME) > 0


def test_config_oasis_actions():
    """OASIS platform actions are defined."""
    from app.config import Config
    assert 'CREATE_POST' in Config.OASIS_TWITTER_ACTIONS
    assert 'CREATE_POST' in Config.OASIS_REDDIT_ACTIONS
    assert 'DO_NOTHING' in Config.OASIS_TWITTER_ACTIONS


def test_config_allowed_extensions():
    """Allowed file extensions are set."""
    from app.config import Config
    assert 'pdf' in Config.ALLOWED_EXTENSIONS
    assert 'md' in Config.ALLOWED_EXTENSIONS
    assert 'txt' in Config.ALLOWED_EXTENSIONS


def test_config_validate():
    """Config.validate returns list of errors."""
    from app.config import Config
    errors = Config.validate()
    assert isinstance(errors, list)
