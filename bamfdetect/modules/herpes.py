from common import Modules, data_strings, load_yara_rules, PEParseModule, ModuleMetadata
from re import compile as recompile, match


class herpes(PEParseModule):
    def __init__(self):
        md = ModuleMetadata(
            module_name="herpes",
            bot_name="Herpes Net",
            description="Botnet that really makes your crotch itch",
            authors=["Brian Wallace (@botnet_hunter)"],
            version="1.0.0",
            date="April 14, 2014",
            references=[]
        )
        PEParseModule.__init__(self, md)
        self.yara_rules = None
        pass

    def _generate_yara_rules(self):
        if self.yara_rules is None:
            self.yara_rules = load_yara_rules("herpes.yara")
        return self.yara_rules

    @staticmethod
    def is_ip_or_domain(s):
        if s[-1] == "/":
            s = s[:-1]
        if s[:7] == "http://":
            s = s[7:]
        p = recompile("^[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]\.[12]?[0-9]?[0-9]$")
        if p.match(s) is not None:
            return True
        # todo IPv6 check
        tlds = ["AC", "ACADEMY", "ACTOR", "AD", "AE", "AERO", "AF", "AG", "AGENCY", "AI", "AL", "AM", "AN", "AO", "AQ",
                "AR", "ARPA",
                "AS", "ASIA", "AT", "AU", "AW", "AX", "AZ", "BA", "BAR", "BARGAINS", "BB", "BD", "BE", "BERLIN", "BEST",
                "BF", "BG",
                "BH", "BI", "BID", "BIKE", "BIZ", "BJ", "BLUE", "BM", "BN", "BO", "BOUTIQUE", "BR", "BS", "BT", "BUILD",
                "BUILDERS",
                "BUZZ", "BV", "BW", "BY", "BZ", "CA", "CAB", "CAMERA", "CAMP", "CARDS", "CAREERS", "CAT", "CATERING",
                "CC", "CD",
                "CENTER", "CEO", "CF", "CG", "CH", "CHEAP", "CHRISTMAS", "CI", "CK", "CL", "CLEANING", "CLOTHING",
                "CLUB", "CM",
                "CN", "CO", "CODES", "COFFEE", "COM", "COMMUNITY", "COMPANY", "COMPUTER", "CONDOS", "CONSTRUCTION",
                "CONTRACTORS",
                "COOL", "COOP", "CR", "CRUISES", "CU", "CV", "CW", "CX", "CY", "CZ", "DANCE", "DATING", "DE",
                "DEMOCRAT", "DIAMONDS",
                "DIRECTORY", "DJ", "DK", "DM", "DNP", "DO", "DOMAINS", "DZ", "EC", "EDU", "EDUCATION", "EE", "EG",
                "EMAIL",
                "ENTERPRISES", "EQUIPMENT", "ER", "ES", "ESTATE", "ET", "EU", "EVENTS", "EXPERT", "EXPOSED", "FARM",
                "FI", "FISH",
                "FJ", "FK", "FLIGHTS", "FLORIST", "FM", "FO", "FOUNDATION", "FR", "FUTBOL", "GA", "GALLERY", "GB", "GD",
                "GE", "GF",
                "GG", "GH", "GI", "GIFT", "GL", "GLASS", "GM", "GN", "GOV", "GP", "GQ", "GR", "GRAPHICS", "GS", "GT",
                "GU", "GUITARS",
                "GURU", "GW", "GY", "HK", "HM", "HN", "HOLDINGS", "HOLIDAY", "HOUSE", "HR", "HT", "HU", "ID", "IE",
                "IL", "IM",
                "IMMOBILIEN", "IN", "INDUSTRIES", "INFO", "INK", "INSTITUTE", "INT", "INTERNATIONAL", "IO", "IQ", "IR",
                "IS", "IT",
                "JE", "JM", "JO", "JOBS", "JP", "KAUFEN", "KE", "KG", "KH", "KI", "KIM", "KITCHEN", "KIWI", "KM", "KN",
                "KOELN", "KP",
                "KR", "KRED", "KW", "KY", "KZ", "LA", "LAND", "LB", "LC", "LI", "LIGHTING", "LIMO", "LINK", "LK", "LR",
                "LS", "LT", "LU",
                "LUXURY", "LV", "LY", "MA", "MAISON", "MANAGEMENT", "MANGO", "MARKETING", "MC", "MD", "ME", "MENU",
                "MG", "MH", "MIL",
                "MK", "ML", "MM", "MN", "MO", "MOBI", "MODA", "MONASH", "MP", "MQ", "MR", "MS", "MT", "MU", "MUSEUM",
                "MV", "MW", "MX",
                "MY", "MZ", "NA", "NAGOYA", "NAME", "NC", "NE", "NET", "NEUSTAR", "NF", "NG", "NI", "NINJA", "NL", "NO",
                "NP", "NR",
                "NU", "NZ", "OKINAWA", "OM", "ONL", "ORG", "PA", "PARTNERS", "PARTS", "PE", "PF", "PG", "PH", "PHOTO",
                "PHOTOGRAPHY",
                "PHOTOS", "PICS", "PINK", "PK", "PL", "PLUMBING", "PM", "PN", "POST", "PR", "PRO", "PRODUCTIONS",
                "PROPERTIES", "PS",
                "PT", "PUB", "PW", "PY", "QA", "QPON", "RE", "RECIPES", "RED", "RENTALS", "REPAIR", "REPORT", "REVIEWS",
                "RICH", "RO",
                "RS", "RU", "RUHR", "RW", "SA", "SB", "SC", "SD", "SE", "SEXY", "SG", "SH", "SHIKSHA", "SHOES", "SI",
                "SINGLES", "SJ",
                "SK", "SL", "SM", "SN", "SO", "SOCIAL", "SOLAR", "SOLUTIONS", "SR", "ST", "SU", "SUPPLIES", "SUPPLY",
                "SUPPORT", "SV",
                "SX", "SY", "SYSTEMS", "SZ", "TATTOO", "TC", "TD", "TECHNOLOGY", "TEL", "TF", "TG", "TH", "TIENDA",
                "TIPS", "TJ", "TK",
                "TL", "TM", "TN", "TO", "TODAY", "TOKYO", "TOOLS", "TP", "TR", "TRAINING", "TRAVEL", "TT", "TV", "TW",
                "TZ", "UA", "UG",
                "UK", "UNO", "US", "UY", "UZ", "VA", "VACATIONS", "VC", "VE", "VENTURES", "VG", "VI", "VIAJES",
                "VILLAS", "VISION",
                "VN", "VOTE", "VOTING", "VOTO", "VOYAGE", "VU", "WANG", "WATCH", "WED", "WF", "WIEN", "WIKI", "WORKS",
                "WS",
                "XN--3BST00M", "XN--3DS443G", "XN--3E0B707E", "XN--45BRJ9C", "XN--55QW42G", "XN--55QX5D", "XN--6FRZ82G",
                "XN--6QQ986B3XL", "XN--80AO21A", "XN--80ASEHDB", "XN--80ASWG", "XN--90A3AC", "XN--C1AVG", "XN--CG4BKI",
                "XN--CLCHC0EA0B2G2A9GCD", "XN--D1ACJ3B", "XN--FIQ228C5HS", "XN--FIQ64B", "XN--FIQS8S", "XN--FIQZ9S",
                "XN--FPCRJ9C3D", "XN--FZC2C9E2C", "XN--GECRJ9C", "XN--H2BRJ9C", "XN--I1B6B1A6A2E", "XN--IO0A7I",
                "XN--J1AMH",
                "XN--J6W193G", "XN--KPRW13D", "XN--KPRY57D", "XN--L1ACC", "XN--LGBBAT1AD8J", "XN--MGB9AWBF",
                "XN--MGBA3A4F16A", "XN--MGBAAM7A8H", "XN--MGBAB2BD", "XN--MGBAYH7GPA", "XN--MGBBH1A71E",
                "XN--MGBC0A9AZCG",
                "XN--MGBERP4A5D4AR", "XN--MGBX4CD0AB", "XN--NGBC5AZD", "XN--NQV7F", "XN--NQV7FS00EMA", "XN--O3CW4H",
                "XN--OGBPF8FL", "XN--P1AI", "XN--PGBS0DH", "XN--Q9JYB4C", "XN--RHQV96G", "XN--S9BRJ9C", "XN--UNUP4Y",
                "XN--WGBH1C", "XN--WGBL6A", "XN--XKC2AL3HYE2A", "XN--XKC2DL3A5EE0H", "XN--YFRO4I67O", "XN--YGBI2AMMX",
                "XN--ZFR164B", "XXX", "XYZ", "YE", "YT", "ZA", "ZM", "ZONE", "ZW"]

        # assume we have a domain now
        if s.find(".") == -1:
            return False
        if s[s.rfind(".") + 1:].upper() in tlds:
            return True
        return False

    def get_bot_information(self, file_data):
        results = {}
        gate = None
        server = None
        for s in data_strings(file_data):
            if s.find("run.php") != -1:
                gate = s
            if s.startswith("http://") and len(s) > len("http://"):
                domain = s[7:]
                if domain.find('/') != -1:
                    domain = domain[:domain.find('/')]
                if herpes.is_ip_or_domain(domain):
                    server = s
            if match(r'^\d\.\d\.\d$', s) is not None:
                        results["version"] = s
        if server is not None and gate is not None:
            results["c2_uri"] = "%s%s" % (server, gate)
        return results


Modules.list.append(herpes())