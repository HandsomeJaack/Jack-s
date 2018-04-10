# -*- mode: python -*-

block_cipher = None


a = Analysis(['Hours\\icon.ico', '10000 hours.py'],
             pathex=['C:\\Users\\PC\\Desktop\\Jack\\10K Hours'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='icon',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\PC\\Desktop\\Jack\\10K')
