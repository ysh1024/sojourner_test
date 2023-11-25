import logging

class CustomServerFormatter(logging.Formatter):
    def format(self, record):
        # user_agent = getattr(record, 'http_user_agent', '-')
        user_agent = getattr(record, 'request').META.get('HTTP_USER_AGENT', '-')

        record.server_time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        return super().format(record) + f' [{user_agent}]'
        # return super().format(record)