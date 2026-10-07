def read_in_wt():

    sio2 = float(input("SiO2: "))
    al2o3 = float(input("Al2O3: "))
    fe2o3 = float(input("Fe2O3: "))
    mgo = float(input("MgO: "))
    cao = float(input("CaO: "))
    k2o = float(input("K2O: "))
    na2o = float(input("Na2O: "))

    components = {
        "sio2" : {
            "wt" : sio2,
            "gmw" : 60.06,
            "charge" : 4,
            "charge_ind" : 4
        },
        "al2o3" : {
            "wt" : al2o3,
            "gmw" : 101.94,
            "charge" : 6,
            "charge_ind" : 3
        },
        "fe2o3" : {
            "wt" : fe2o3,
            "gmw" : 159.68,
            "charge" : 6,
            "charge_ind" : 3
        },
        "mgo" : {
            "wt" : mgo,
            "gmw" : 40.32,
            "charge" : 2,
            "charge_ind" : 2
        },
        "cao" : {
            "wt" : cao,
            "gmw" : 56.08,
            "charge" : 2,
            "charge_ind" : 2
        },                
        "k2o" : {
            "wt" : k2o,
            "gmw" : 94.19,
            "charge" : 2,
            "charge_ind" : 1
        },
        "na2o" : {
            "wt" : na2o,
            "gmw" : 62.00,
            "charge" : 2,
            "charge_ind" : 1
        },
    }

    return components


def calculate_atoms(components: dict):

    total = 0
    for component in components.values():
        geq_cat = component["wt"] / component["gmw"] * component["charge"]
        component["geq_cat"] = geq_cat
        total += geq_cat
 
    for component in components.values():
        geq = component["geq_cat"] / total * 22
        component["geq"] = geq

        atoms = component["geq"] / component["charge_ind"]
        component["atoms"] = atoms

    return components


def create_formula(components: dict):

    formula = ""

    i = f"Ca{components['cao']['atoms']:.3f} K{components['k2o']['atoms']:.3f} Na{components['na2o']['atoms']:.3f} "
    formula += i

    if components["sio2"]["atoms"] >= 4:
        al2 = 0
    else:
        al2 = (4 - components['sio2']['atoms'])
    al1 = components['al2o3']['atoms'] - al2

    o = f"[(Al{al1:.3f} Mg{components['mgo']['atoms']:.3f} Fe{components['fe2o3']['atoms']:.3f}) "
    formula += o

    t = f"(Si{components['sio2']['atoms']:.3f} Al{al2:.3f})] O10 (OH)2"
    formula += t

    return formula


def main():

    print("===Enter wt%===")

    components = read_in_wt()
    components = calculate_atoms(components)
    formula = create_formula(components)

    print("Formula:", formula)


if __name__ == '__main__':
    main()