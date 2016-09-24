import yaml
import trafaret as t


HostPort = t.Tuple(t.String, t.Int)
Unixsocket = t.String
HostPortDict = t.Dict({
    t.Key('host'): t.String,
    t.Key('port'): t.Int,
    })

postgres_trafaret = t.Forward()

config_trafaret = t.Dict({
    t.Key('debug'): t.Bool,
    t.Key('host', default='localhost'): t.String,
    t.Key('port', default=5000): t.Int[1025:65535],
    t.Key('postgres'): postgres_trafaret,
    t.Key('redis'): t.Dict({
        t.Key('address', default=('localhost', 6379)): t.Or(
            HostPort,
            HostPortDict,
            Unixsocket,
        }),
    })


postgres_trafaret << t.Dict({
    t.Key('host', default='localhost'): t.String,
    t.Key('port', default=5432): t.Int,
    t.Key('user', default='test'): t.String,
    t.Key('password', default='test'): t.String,
    t.Key('db_name', default='test'): t.String,
    t.Key('echo', default=False): t.Bool,
    })


def load_config(fname):
    with open(fname, 'rt') as f:
        return config_trafaret(yaml.load(f))
