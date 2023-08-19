from log import logger
from tkapp import App


if __name__ == '__main__':
    logger.info('--- START OF PROGRAM ---')

    app = App()
    app.mainloop()

    logger.info('--- END OF PROGRAM ---\n')
