from sources.csp import CSP


canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })


def main():
    print(sorted(canterbury_colouring.var_domains['christchurch']))
    print(sorted(canterbury_colouring.var_domains['selwyn']))
    print(sorted(canterbury_colouring.var_domains['waimakariri']))


if __name__ == "__main__":
    main()
