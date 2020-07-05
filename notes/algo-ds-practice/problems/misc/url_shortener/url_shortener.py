from problems.misc.url_shortener.id_service import IdService


class UrlShortener:
    def __init__(self, charset=None):
        if charset:
            self.charset = charset
        else:
            self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            self.charset_encoding = charset
            self.charset_decoding = {}
            for idx, char in enumerate(self.charset):
                self.charset_decoding[char] = idx
        self.map_short_to_long = {}
        # We are using an auto-incremental id service because we want to assign
        # different ids to even the same url.
        # Example: Microsoft gives a short-url `goo.gl/infy` to Infosys and `goo.gl/tcs`
        # to TCS, both pointing `microsoft.com` to see how many click are coming from
        # both separately.
        self.id_service = IdService()

    def _get_decimal_from_string(self, input_string):
        return self.id_service.get_next_id()

    def _get_encoded(self, decimal):
        if decimal == 0:
            return self.charset[0]
        encoded_reverse = ''
        encoding_base = len(self.charset)
        while decimal:
            remainder = decimal % encoding_base
            encoded_reverse += self.charset[remainder]
            decimal //= encoding_base
        encoded = encoded_reverse[::-1]
        return encoded

    def _get_decoded(self, encoded):
        decoded = 0
        encoding_base = len(self.charset)
        for encoded_char in encoded:
            encoded_char_value = self.charset_decoding[encoded_char]
            decoded = decoded * encoding_base + encoded_char_value
        return decoded

    def shorten(self, long_url):
        long_url_decimal = self._get_decimal_from_string(long_url)
        short_url = self._get_encoded(long_url_decimal)
        self.map_short_to_long[short_url] = long_url
        return short_url

    def elongate(self, short_url):
        return self.map_short_to_long[short_url]

    def remove(self, short_url):
        '''
        This probably doesn't happen at all in real-life shorteners.
        '''
        del self.map_short_to_long[short_url]
        short_url_decoded = self._get_decoded(short_url)
        self.id_service.delete_id(short_url_decoded)


def main():
    shorty = UrlShortener()
    shortened = shorty.shorten('google.com')
    shortened = shorty.shorten('google.com')
    shortened = shorty.shorten('google.com')
    shortened = shorty.shorten('google.com')
    print(shortened)
    print(shorty.elongate(shortened))
    shorty.remove('0')
    shortened = shorty.shorten('googleasa.com')
    print(shorty.elongate('0'))


if __name__ == "__main__":
    main()
