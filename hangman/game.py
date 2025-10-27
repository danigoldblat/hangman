def init_state(secret: str, max_tries: int) -> dict:
    {
        "secret":str,
        "display":list[str],
        "guessed":set[str],
        "guesses_wrong":int,
        "max_tries":int
    }
    {
        "secret":secret,
        "display":list[str],
        "guessed":set[str],
        "guesses_wrong":int,
        "max_tries":7
    }