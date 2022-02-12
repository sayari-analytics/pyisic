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
    with open("standards.json", "w") as outfile:
        json.dump(
            {key: val for key, val in pyisic.__dict__.items() if isinstance(val, pyisic.types.Standard)},
            outfile,
            cls=StandardEncoder,
            sort_keys=True,
            indent=4,
        )
