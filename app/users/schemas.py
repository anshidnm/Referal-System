from drf_spectacular.utils import extend_schema


class Documentation:
    """
    Utility class for api documentaion
    """
    
    REGISTER = extend_schema(
        tags=["AUTH"],
        summary="API for user registration",
        description="""
            email, name and password should be
            pass as payload.
            If any referal code availabe it also
            can pass as payload.
            If everything success user id and tokens should be returned
            with 200 status code.
        """
    )

    LOGIN = extend_schema(
        tags=["AUTH"],
        summary="API for user login",
        description="""
            email and password should be
            pass as payload.
            If everything success tokens should be returned
            with 200 status code.
        """
    )

    REFRESH = extend_schema(
        tags=["AUTH"],
        summary="API for refresh token",
        description="""
            refresh token should be
            pass as payload.
            If it is a valid token then a new
            access token should be return.
        """
    )

    MY_DETAILS = extend_schema(
        tags=["DETAILS"],
        summary="API for user details",
        description="""
            Returns the full details of current user
        """
    )

    REFERALS = extend_schema(
        tags=["REFERALS"],
        summary="API for list all referals",
        description="""
            Returns the  details of users
            who are registerd with current user's 
            referal code.
            The response should be a paginated response
            with next page url, prev page url, total page count
            and total referals count
        """
    )