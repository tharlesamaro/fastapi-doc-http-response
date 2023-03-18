> To read this README in English, click [here](https://github.com/tharlesamaro/fastapi-doc-http-response).

## FastAPI Doc HTTP Response

<tr>
    <td>
      <a href="https://codecov.io/gh/tharlesamaro/fastapi-doc-http-response">
        <img src="https://codecov.io/gh/tharlesamaro/fastapi-doc-http-response/branch/main/graph/badge.svg?token=VAY93FNZCA" alt="codecov">
      </a>
    </td>
    <td>
      <a href="https://pypi.org/project/fastapi-doc-http-response">
        <img src="https://img.shields.io/pypi/v/fastapi_doc_http_response?color=blue" alt="pypi">
      </a>
    </td>
</tr>

O FastAPI Doc HTTP Response é um pacote Python que facilita a definição de respostas HTTP padrão para APIs FastAPI e permite adicionar facilmente retornos HTTP na documentação da API. Com este pacote, é possível criar facilmente respostas padrão para os códigos de status HTTP mais comuns.

O FastAPI oferece documentação automática para as suas rotas, incluindo as respostas HTTP esperadas para cada rota. Por padrão, o FastAPI inclui apenas alguns códigos de retorno HTTP na documentação. Com o FastAPI Doc HTTP Response, você pode adicionar facilmente outros códigos de retorno HTTP, garantindo que a documentação da sua API seja completa e precisa.

### Instalação

Você pode instalar o FastAPI Doc HTTP Response usando o pip:

```bash
pip install fastapi-doc-http-response
```

### Uso

Para usar o FastAPI Doc HTTP Response em sua aplicação FastAPI, basta importar a função `get_responses` do pacote e chamá-la com uma lista de códigos de status HTTP que você deseja definir:

```python
from fastapi import FastAPI
from fastapi_doc_http_response import get_responses

app = FastAPI()


@app.get("/xpto", responses=get_responses(201, 400, 401, 403))
async def xpto():
    # ...
```

O código acima irá definir as seguintes respostas HTTP padrão para a rota `/xpto`:

- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden

Esses códigos de retorno também serão adicionados automaticamente à documentação da API gerada pelo FastAPI.

Note que não se faz necessário definir um código de retorno HTTP para o status 200 OK e o status 422 Unprocessable Entity, pois eles já são definidos por padrão pelo FastAPI.

### Códigos de retorno HTTP suportados

Os códigos de retorno HTTP suportados pelo FastAPI Doc HTTP Response são:

- 100 Continue
- 201 Created
- 202 Accepted
- 203 Non-Authoritative Information
- 204 No Content
- 206 Partial Content
- 207 Multi-Status
- 208 Already Reported
- 226 IM Used
- 300 Multiple Choices
- 301 Moved Permanently
- 302 Found
- 303 See Other
- 304 Not Modified
- 305 Use Proxy
- 306 Switch Proxy
- 307 Temporary Redirect
- 308 Permanent Redirect
- 400 Bad Request
- 401 Unauthorized
- 402 Payment Required
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 406 Not Acceptable
- 407 Proxy Authentication Required
- 408 Request Timeout
- 409 Conflict
- 410 Gone
- 411 Length Required
- 412 Precondition Failed
- 413 Payload Too Large
- 414 URI Too Long
- 416 Range Not Satisfiable
- 417 Expectation Failed
- 418 I'm a teapot
- 420 Enhance Your Calm
- 423 Locked
- 424 Failed Dependency
- 425 Unordered Collection
- 426 Upgrade Required
- 429 Too Many Requests
- 431 Request Header Fields Too Large
- 444 No Response
- 449 Retry With
- 450 Blocked by Windows Parental Controls
- 451 Unavailable For Legal Reasons
- 494 Request Header Too Large
- 500 Internal Server Error

### Licença
Este pacote é licenciado sob a [MIT License](https://opensource.org/license/mit/). Consulte o arquivo [LICENSE](https://github.com/tharlesamaro/fastapi-doc-http-response/blob/main/LICENSE) para obter mais informações.
