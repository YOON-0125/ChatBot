TOPIC_RESPONSES = {
    '/sports': 'You selected sports.',
    '/music': 'You selected music.',
    '/science': 'You selected science.'
}


def get_response(path: str) -> str:
    """Return the predefined response for a topic path."""
    return TOPIC_RESPONSES.get(path, 'Unknown topic.')
