def JDdelete():
    try:
        return {}
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }