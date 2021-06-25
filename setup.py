from cx_Freeze import setup, Executable

setup(
    name="IMED_Soletrando",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["hit_or_fail", "images"]
        }},
    executables= [Executable (script="game.py")],
)