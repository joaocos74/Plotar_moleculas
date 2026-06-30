from rdkit import Chem
from rdkit.Chem import Draw

# Defina a SMILES que você deseja visualizar
smiles = '[C@@H](O)[CH2][O]'

# Crie um objeto de molécula a partir da SMILES
mol = Chem.MolFromSmiles(smiles)

# Desenhe a molécula
img = Draw.MolToImage(mol)

# Exiba a imagem
print(img)