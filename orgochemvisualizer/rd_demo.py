from rdkit import Chem

mol = Chem.MolFromSmiles('Cl[C@H](F)NC\C=C\C')
rdkit.Chem.AllChem.Compute2DCoords(mol)
for c in mol.GetConformers():
    print(c.GetPositions())