"""Resource: Implemented the needed portions of restkit.Resource that pigshare needs.

Does not impleented the ull functionality of restkit.Resource, just what pigshare
needs.

restkit has not been ported to Python3 and appears to be abandoned. See:
    https://github.com/benoitc/restkit/issues/47

"""

# https://requests.readthedocs.io/en/master/
import requests

class Resource:

    def __init__(self, uri):
        self.uri = uri

    def get(self, path=None, headers=None, params_dict=None, **params):
        """ HTTP GET
        - path: string  additionnal path to the uri
        - headers: dict, optionnal headers that will
            be added to HTTP request.
        - params: Optionnal parameterss added to the request.
        """
        return self.request("GET", path=path, headers=headers,
                params_dict, **params)

    def post(self, path=None, payload=None, headers=None,
            params_dict=None, **params):
        """ HTTP POST
        - payload: string passed to the body of the request
        - path: string  additionnal path to the uri
        - headers: dict, optionnal headers that will
            be added to HTTP request.
        - params: Optionnal parameterss added to the request
        """

        return self.request("POST", path=path, payload=payload,
                            headers=headers, params)

    def put(self, path=None, payload=None, headers=None,
            params_dict=None, **params):
        """ HTTP PUT
        see POST for params description.
        """
        return self.request("PUT", path=path, payload=payload,
                        headers=headers, params_dict=params_dict, **params)

    def delete(self, path=None, headers=None, params_dict=None, **params):
        """ HTTP DELETE
        see GET for params description.
        """
        return self.request("DELETE", path=path, headers=headers,
                params_dict=params_dict, **params)


