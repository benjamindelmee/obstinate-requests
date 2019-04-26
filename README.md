# ![Obstinate Requests](misc/obstinate_requests.png)

Obstinate Requests is a python snippet wrapping the [requests](https://github.com/kennethreitz/requests) library.

Obstinate automaticaly replays a request when a connection error occurs, or when the status code returned by the server is not the expected one.

**Why / when to use Obstinate?**

When you want to send a request through Internet but you have an instable connexion, or when the server you query is busy, you sometimes need to replay multiple times the request before it works. For instance, this happens a lot to data scientists willing to grab data from a publicly accessible database. 

However, if the connection between your application and the remote server is critical, you'd better to implement a tailor-made solution in order to handle edge scenarios.