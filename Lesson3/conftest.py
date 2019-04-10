def pytest_collection_modifyitems(items, config):
    use_url = config.option.useurls
    check_urls(use_url)
    if use_url is not None:
        use_url_lst = use_url.split(",")
        selected_items = []
        deselected_items = []

        for item in items:
            marker = item.get_closest_marker("site_type")
            print(marker)
            if marker.args[0] in use_url_lst:
                selected_items.append(item)
            else:
                deselected_items.append(item)

        config.hook.pytest_deselected(items=deselected_items)
        items[:] = selected_items

def pytest_addoption(parser):
    parser.addoption("--useurls", action="store", default=None, help="Enter tested urls, separate them by comma")

def check_urls(use_url):
    good_urls = ("https://api.cdnjs.com","https://api.openbrewerydb.org","https://dog.ceo/api")

    if use_url is None:
        raise ValueError('You must specify --useurls parameter.')

    use_url_lst = use_url.split(",")
    for url_str in use_url_lst:
        if url_str not in good_urls:
            raise ValueError('Unsupported --useurls value. Suported values: ' + good_urls.__str__())
