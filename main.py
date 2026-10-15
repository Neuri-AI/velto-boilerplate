import sys
from velto import VeltoContext
from velto.ui import psx

class ${class_name}(VeltoContext):

    def render(self):
        return psx("""
            <Flex direction="column">
                <Text>Hello, World!</Text>
            </Flex>
        """)

if __name__ == "__main__":
    sys.exit(${class_name}().run())