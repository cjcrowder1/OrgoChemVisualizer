# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# pyinstaller orgochemvisualizer/__main__.py \
#    --onefile --clean \
#    -p orgochemvisualizer/  \
#    -n OrgoExe

a = Analysis(['orgochemvisualizer/__main__.py'],
             pathex=['orgochemvisualizer/', '/home/peastham/Desktop/UROP-projects/OrgoChemVisualizer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='OrgoExe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
