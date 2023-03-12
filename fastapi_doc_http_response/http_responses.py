from typing import Any

CONTENT_DEFAULT: dict[str, dict[str, Any]] = {
    "application/json": {"example": {"detail": "string"}}
}


def _create_response_dict(
    description: str, content: dict[str, dict[str, Any]] = CONTENT_DEFAULT
) -> dict[str, Any]:
    return {"content": content, "description": description}


HTTP_RESPONSES: dict[str, dict[str, Any]] = {
    "100": _create_response_dict(description="Continue"),
    "201": _create_response_dict(description="Created"),
    "202": _create_response_dict(description="Accepted"),
    "203": _create_response_dict(description="Non-Authoritative Information"),
    "204": _create_response_dict(description="No Content"),
    "206": _create_response_dict(description="Partial Content"),
    "207": _create_response_dict(description="Multi-Status"),
    "208": _create_response_dict(description="Already Reported"),
    "226": _create_response_dict(description="IM Used"),
    "300": _create_response_dict(description="Multiple Choices"),
    "301": _create_response_dict(description="Moved Permanently"),
    "302": _create_response_dict(description="Found"),
    "303": _create_response_dict(description="See Other"),
    "304": _create_response_dict(description="Not Modified"),
    "305": _create_response_dict(description="Use Proxy"),
    "306": _create_response_dict(description="Switch Proxy"),
    "307": _create_response_dict(description="Temporary Redirect"),
    "308": _create_response_dict(description="Permanent Redirect"),
    "400": _create_response_dict(description="Bad Request"),
    "401": _create_response_dict(description="Unauthorized"),
    "402": _create_response_dict(description="Payment Required"),
    "403": _create_response_dict(description="Forbidden"),
    "404": _create_response_dict(description="Not Found"),
    "405": _create_response_dict(description="Method Not Allowed"),
    "406": _create_response_dict(description="Not Acceptable"),
    "407": _create_response_dict(description="Proxy Authentication Required"),
    "408": _create_response_dict(description="Request Timeout"),
    "409": _create_response_dict(description="Conflict"),
    "410": _create_response_dict(description="Gone"),
    "411": _create_response_dict(description="Length Required"),
    "412": _create_response_dict(description="Precondition Failed"),
    "413": _create_response_dict(description="Payload Too Large"),
    "414": _create_response_dict(description="URI Too Long"),
    "416": _create_response_dict(description="Range Not Satisfiable"),
    "417": _create_response_dict(description="Expectation Failed"),
    "418": _create_response_dict(description="I'm a teapot"),
    "420": _create_response_dict(description="Enhance Your Calm"),
    "423": _create_response_dict(description="Locked"),
    "424": _create_response_dict(description="Failed Dependency"),
    "425": _create_response_dict(description="Unordered Collection"),
    "426": _create_response_dict(description="Upgrade Required"),
    "429": _create_response_dict(description="Too Many Requests"),
    "431": _create_response_dict(description="Request Header Fields Too Large"),
    "444": _create_response_dict(description="No Response"),
    "449": _create_response_dict(description="Retry With"),
    "450": _create_response_dict(description="Blocked by Windows Parental Controls"),
    "451": _create_response_dict(description="Unavailable For Legal Reasons"),
    "494": _create_response_dict(description="Request Header Too Large"),
    "500": _create_response_dict(
        description="Internal Server Error",
        content={"application/json": {"example": "string"}},
    ),
    # more http responses here
}


def get_responses(*args: int | str) -> dict[str, dict[str, Any]] | None:
    responses = {}
    for arg in args:
        response = HTTP_RESPONSES.get(str(arg))
        if response:
            responses[str(arg)] = response
    return responses or None
