from formula import parse_formula


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.

    # Return the total molar mass.
    SYMBOL_INDEX = 0
    QUANTITY_INDEX = 1
    ATOMIC_MASS_INDEX = 1
    total_molar_mass = 0
    for i in symbol_quantity_list:
        symbol = i[SYMBOL_INDEX]
        quantity = i[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass


def make_periodic_table():
    """Return a dictionary for the periodic table elements

    Returns:
        dictionary: as requested in assignment
    """
    list_non_formatted = [
        "Ac",	"Actinium",	227,
        "Ag",	"Silver",	107.8682,
        "Al",	"Aluminum",	26.9815386,
        "Ar",	"Argon",	39.948,
        "As",	"Arsenic",	74.9216,
        "At",	"Astatine",	210,
        "Au",	"Gold",	196.966569,
        "B",	"Boron",	10.811,
        "Ba",	"Barium",	137.327,
        "Be",	"Beryllium",	9.012182,
        "Bi",	"Bismuth",	208.9804,
        "Br",	"Bromine",	79.904,
        "C",	"Carbon",	12.0107,
        "Ca",	"Calcium",	40.078,
        "Cd",	"Cadmium",	112.411,
        "Ce",	"Cerium",	140.116,
        "Cl",	"Chlorine",	35.453,
        "Co",	"Cobalt",	58.933195,
        "Cr",	"Chromium",	51.9961,
        "Cs",	"Cesium",	132.9054519,
        "Cu",	"Copper",	63.546,
        "Dy",	"Dysprosium",	162.5,
        "Er",	"Erbium",	167.259,
        "Eu",	"Europium",	151.964,
        "F",	"Fluorine",	18.9984032,
        "Fe",	"Iron",	55.845,
        "Fr",	"Francium",	223,
        "Ga",	"Gallium",	69.723,
        "Gd",	"Gadolinium",	157.25,
        "Ge",	"Germanium",	72.64,
        "H",	"Hydrogen",	1.00794,
        "He",	"Helium",	4.002602,
        "Hf",	"Hafnium",	178.49,
        "Hg",	"Mercury",	200.59,
        "Ho",	"Holmium",	164.93032,
        "I",	"Iodine",	126.90447,
        "In",	"Indium",	114.818,
        "Ir",	"Iridium",	192.217,
        "K",	"Potassium",	39.0983,
        "Kr",	"Krypton",	83.798,
        "La",	"Lanthanum",	138.90547,
        "Li",	"Lithium",	6.941,
        "Lu",	"Lutetium",	174.9668,
        "Mg",	"Magnesium",	24.305,
        "Mn",	"Manganese",	54.938045,
        "Mo",	"Molybdenum",	95.96,
        "N",	"Nitrogen",	14.0067,
        "Na",	"Sodium",	22.98976928,
        "Nb",	"Niobium",	92.90638,
        "Nd",	"Neodymium",	144.242,
        "Ne",	"Neon",	20.1797,
        "Ni",	"Nickel",	58.6934,
        "Np",	"Neptunium",	237,
        "O",	"Oxygen",	15.9994,
        "Os",	"Osmium",	190.23,
        "P",	"Phosphorus",	30.973762,
        "Pa",	"Protactinium",	231.03588,
        "Pb",	"Lead",	207.2,
        "Pd",	"Palladium",	106.42,
        "Pm",	"Promethium",	145,
        "Po",	"Polonium",	209,
        "Pr",	"Praseodymium",	140.90765,
        "Pt",	"Platinum",	195.084,
        "Pu",	"Plutonium",	244,
        "Ra",	"Radium",	226,
        "Rb",	"Rubidium",	85.4678,
        "Re",	"Rhenium",	186.207,
        "Rh",	"Rhodium",	102.9055,
        "Rn",	"Radon",	222,
        "Ru",	"Ruthenium",	101.07,
        "S",	"Sulfur",	32.065,
        "Sb",	"Antimony",	121.76,
        "Sc",	"Scandium",	44.955912,
        "Se",	"Selenium",	78.96,
        "Si",	"Silicon",	28.0855,
        "Sm",	"Samarium",	150.36,
        "Sn",	"Tin",	118.71,
        "Sr",	"Strontium",	87.62,
        "Ta",	"Tantalum",	180.94788,
        "Tb",	"Terbium",	158.92535,
        "Tc",	"Technetium",	98,
        "Te",	"Tellurium",	127.6,
        "Th",	"Thorium",	232.03806,
        "Ti",	"Titanium",	47.867,
        "Tl",	"Thallium",	204.3833,
        "Tm",	"Thulium",	168.93421,
        "U",	"Uranium",	238.02891,
        "V",	"Vanadium",	50.9415,
        "W",	"Tungsten",	183.84,
        "Xe",	"Xenon",	131.293,
        "Y",	"Yttrium",	88.90585,
        "Yb",	"Ytterbium",	173.054,
        "Zn",	"Zinc",	65.38,
        "Zr",	"Zirconium",	91.224
    ]
    dict_periodic_table = {}
    i = 0
    for i in range (0,len(list_non_formatted)-1,3):
        # Indexes for inner lists in a symbol_quantity_list
        SYMBOL_INDEX = i
        NAME_INDEX = i+1
        ATOMIC_MASS_INDEX = i+2
        dict_periodic_table[list_non_formatted[SYMBOL_INDEX]] = [list_non_formatted[NAME_INDEX],list_non_formatted[ATOMIC_MASS_INDEX]]
    return dict_periodic_table

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    if formula in known_molecules_dict:
        return known_molecules_dict[formula]

def main():
    # Get a chemical formula for a molecule from the user.

    # Get the mass of a chemical sample in grams from the user.

    # Call the make_periodic_table function and
    # store the periodic table in a variable.

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.

    # Compute the number of moles in the sample.

    # Print the molar mass.

    # Print the number of moles.

    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    periodic_table = make_periodic_table()
    molecular_formula = input("Enter the molecular formula of the sample: ")
    mass_sample = float(input("Enter the mass in grams of the sample: "))
    molar_mass = compute_molar_mass(parse_formula(molecular_formula,periodic_table), periodic_table)
    print(f"{molar_mass} grams/mole")
    print(f"{round(mass_sample/molar_mass,5)} moles")
    print(f"{get_formula_name(molecular_formula, known_molecules_dict)}")


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()