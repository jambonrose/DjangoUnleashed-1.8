class PageLinksMixin:
    page_kwarg = 'page'

    def _page_urls(self, page_number):
        return "?{pkw}={n}".format(
            pkw=self.page_kwarg,
            n=page_number)

    def first_page(self, page):
        # don't show on first page
        if page.number > 1:
            return self._page_urls(1)
        return None

    def previous_page(self, page):
        if (page.has_previous()
                and page.number > 2):
            return self._page_urls(
                page.previous_page_number())
        return None

    def next_page(self, page):
        last_page = page.paginator.num_pages
        if (page.has_next()
                and page.number < last_page - 1):
            return self._page_urls(
                page.next_page_number())
        return None

    def last_page(self, page):
        last_page = page.paginator.num_pages
        if page.number < last_page:
            return self._page_urls(last_page)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs)
        page = context.get('page_obj')
        if page is not None:
            context.update({
                'first_page_url':
                    self.first_page(page),
                'previous_page_url':
                    self.previous_page(page),
                'next_page_url':
                    self.next_page(page),
                'last_page_url':
                    self.last_page(page),
            })
        return context
