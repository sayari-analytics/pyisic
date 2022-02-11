import json
import zipfile

import pyisic


class StandardEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pyisic.types.Category):
            return obj.name

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    standards = {key: val for key, val in pyisic.__dict__.items() if isinstance(val, pyisic.types.Standard)}

    with zipfile.ZipFile("data.zip", "w") as outfile:
        outfile.writestr("standards.json", json.dumps(standards, cls=StandardEncoder, sort_keys=True, indent=4))
