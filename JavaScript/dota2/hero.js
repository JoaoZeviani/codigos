class Hero {
    constructor(id, localized_name, name, primary_attr, attack_type, roles) {
        this.id = id;
        this.localized_name = localized_name;
        this.name = name;
        this.primary_attr = primary_attr;
        this.attack_type = attack_type;
        this.roles = roles;
    }

    getPrimaryAttrFullName() {
        const attrMap = {
            'agi': 'Agility',
            'str': 'Strength',
            'int': 'Intelligence',
            'all': 'Universal'
        };
        return attrMap[this.primary_attr];
    }
}
