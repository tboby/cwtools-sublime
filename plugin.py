import os

import shutil

import sublime_plugin

import sublime

from LSP.plugin.core.handlers import LanguageHandler

from LSP.plugin.core.settings import ClientConfig

from LSP.plugin.core.protocol import Request, Point

from LSP.plugin.references import ensure_references_panel

from LSP.plugin.core.clients import client_for_view

from LSP.plugin.core.documents import is_at_word, get_position, get_document_position

from LSP.plugin.core.configurations import is_supported_view

from LSP.plugin.core.workspace import get_project_path

from LSP.plugin.core.url import uri_to_filename

from os.path import dirname


default_cwtools_settings = {
        'localisation': {
                'languages' : ''
        },
        'errors': {
            'vanilla': 'false',
            'ignore': '',
            'ignorefiles': ''
        },
        'experimental' : 'false',
        'experimental_completion': 'true',
        'trace': {
            'server': 'messages'
        }
}

config_name = 'cwtools'

server_name = 'cwtools'

def get_cwtools_config():
    s = sublime.load_settings("LSP-cwtools.sublime-settings").get('settings', default_cwtools_settings)
    return ClientConfig(

        name=config_name,

        binary_args=[

            dirname(__file__) + '/win-x64/Main.exe'

        ],

        tcp_port=None,

        scopes=['source.stellaris'],

        syntaxes=[

           'Packages/StellarisSublime/Stellaris.sublime-syntax',

        ],

        languageId='stellaris',

        enabled=False,

        init_options=dict(),

        settings=s,

        env=dict())


class LspCwtoolsPlugin(LanguageHandler):
    def __init__(self):
        self._name = config_name
        self._config = get_cwtools_config()



    @property
    def name(self) -> str:
        return self._name



    @property
    def config(self) -> ClientConfig:
        return self._config



    def on_start(self, window) -> bool:
        return True



    def on_initialized(self, client) -> None:
        return




