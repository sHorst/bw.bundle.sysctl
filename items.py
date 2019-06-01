

if 'sysctl' in node.metadata:
    content = '\n'.join(['{}={}'.format(k, v) for k, v in node.metadata.get('sysctl', {}).items()]) + "\n"

    files = {
        "/etc/sysctl.conf": {
            'content': content,
            'owner': "root",
            'group': "root",
            'mode': "0644"
        },
    }
