from pages.base_page import Page


class SignInPage(Page):

    def sign_in_page_title(self, title):
        page_title = self.get_title(title)
        assert page_title == "Amazon Sign-In", 'expected title doesnt match with actual title '




