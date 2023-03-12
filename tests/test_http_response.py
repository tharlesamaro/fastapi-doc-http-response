from fastapi_doc_http_response.http_responses import (
    CONTENT_DEFAULT,
    HTTP_RESPONSES,
    _create_response_dict,
    get_responses,
)


def test_http_responses_descriptions():
    assert HTTP_RESPONSES["100"]["description"] == "Continue"
    assert HTTP_RESPONSES["201"]["description"] == "Created"
    assert HTTP_RESPONSES["202"]["description"] == "Accepted"
    assert HTTP_RESPONSES["203"]["description"] == "Non-Authoritative Information"
    assert HTTP_RESPONSES["204"]["description"] == "No Content"
    assert HTTP_RESPONSES["206"]["description"] == "Partial Content"
    assert HTTP_RESPONSES["207"]["description"] == "Multi-Status"
    assert HTTP_RESPONSES["208"]["description"] == "Already Reported"
    assert HTTP_RESPONSES["226"]["description"] == "IM Used"
    assert HTTP_RESPONSES["300"]["description"] == "Multiple Choices"
    assert HTTP_RESPONSES["301"]["description"] == "Moved Permanently"
    assert HTTP_RESPONSES["302"]["description"] == "Found"
    assert HTTP_RESPONSES["303"]["description"] == "See Other"
    assert HTTP_RESPONSES["304"]["description"] == "Not Modified"
    assert HTTP_RESPONSES["305"]["description"] == "Use Proxy"
    assert HTTP_RESPONSES["306"]["description"] == "Switch Proxy"
    assert HTTP_RESPONSES["307"]["description"] == "Temporary Redirect"
    assert HTTP_RESPONSES["308"]["description"] == "Permanent Redirect"
    assert HTTP_RESPONSES["400"]["description"] == "Bad Request"
    assert HTTP_RESPONSES["401"]["description"] == "Unauthorized"
    assert HTTP_RESPONSES["402"]["description"] == "Payment Required"
    assert HTTP_RESPONSES["403"]["description"] == "Forbidden"
    assert HTTP_RESPONSES["404"]["description"] == "Not Found"
    assert HTTP_RESPONSES["405"]["description"] == "Method Not Allowed"
    assert HTTP_RESPONSES["406"]["description"] == "Not Acceptable"
    assert HTTP_RESPONSES["407"]["description"] == "Proxy Authentication Required"
    assert HTTP_RESPONSES["408"]["description"] == "Request Timeout"
    assert HTTP_RESPONSES["409"]["description"] == "Conflict"
    assert HTTP_RESPONSES["410"]["description"] == "Gone"
    assert HTTP_RESPONSES["411"]["description"] == "Length Required"
    assert HTTP_RESPONSES["412"]["description"] == "Precondition Failed"
    assert HTTP_RESPONSES["413"]["description"] == "Payload Too Large"
    assert HTTP_RESPONSES["414"]["description"] == "URI Too Long"
    assert HTTP_RESPONSES["416"]["description"] == "Range Not Satisfiable"
    assert HTTP_RESPONSES["417"]["description"] == "Expectation Failed"
    assert HTTP_RESPONSES["418"]["description"] == "I'm a teapot"
    assert HTTP_RESPONSES["420"]["description"] == "Enhance Your Calm"
    assert HTTP_RESPONSES["423"]["description"] == "Locked"
    assert HTTP_RESPONSES["424"]["description"] == "Failed Dependency"
    assert HTTP_RESPONSES["425"]["description"] == "Unordered Collection"
    assert HTTP_RESPONSES["426"]["description"] == "Upgrade Required"
    assert HTTP_RESPONSES["429"]["description"] == "Too Many Requests"
    assert HTTP_RESPONSES["431"]["description"] == "Request Header Fields Too Large"
    assert HTTP_RESPONSES["444"]["description"] == "No Response"
    assert HTTP_RESPONSES["449"]["description"] == "Retry With"
    assert HTTP_RESPONSES["450"]["description"] == "Blocked by Windows Parental Controls"
    assert HTTP_RESPONSES["451"]["description"] == "Unavailable For Legal Reasons"
    assert HTTP_RESPONSES["494"]["description"] == "Request Header Too Large"
    assert HTTP_RESPONSES["500"]["description"] == "Internal Server Error"

def test_get_http_responses_empty():
        assert get_responses() is None

def test_get_http_responses_not_found():
    assert get_responses(200) is None

def test_get_http_responses_found():
    response = get_responses(400)
    assert response == {"400": HTTP_RESPONSES["400"]}

def test_create_http_response_dict_default():
    response_dict = _create_response_dict(description="test")
    assert response_dict == {
        "content": CONTENT_DEFAULT,
        "description": "test"
    }

def test_create_response_dict_custom_content():
    custom_content = {"application/json": {"example": {"value": "string"}}}
    response_dict = _create_response_dict(
        description="test", content=custom_content
    )
    assert response_dict == {
        "content": custom_content,
        "description": "test"
    }