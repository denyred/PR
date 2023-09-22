from player import Player
import xml.etree.ElementTree as ET
import player_pb2 as player_protobf

class PlayerFactory:
    def to_json(self, players):
        data = []
        for i in players:
            data.append({'nickname':i.nickname,
                    'email': i.email,
                    'date_of_birth': i.date_of_birth.strftime("%Y-%m-%d"),
                    'xp': i.xp,
                    'class':i.cls

                    })
        return data
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        pass

    def from_json(self, list_of_dict):
        data = []
        for obj in list_of_dict:
            local = Player(obj['nickname'],obj['email'],obj['date_of_birth'],obj['xp'],obj['class'])
            data.append(local)
        return data
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        pass

    def from_xml(self, xml_string):
        root = ET.fromstring(xml_string)

        players = []

        for local_player in root.findall("player"):
            nickname = local_player.find("nickname").text
            email = local_player.find("email").text
            date_of_birth = local_player.find("date_of_birth").text
            xp = int(local_player.find("xp").text)
            cls = local_player.find("class").text

            player = Player(nickname, email, date_of_birth, xp, cls)
            players.append(player)

        return players
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        pass

    def to_xml(self, list_of_players):
        data = ET.Element("data")

        for player in list_of_players:
            local_player = ET.SubElement(data, "player")
            nickname = ET.SubElement(local_player, "nickname")
            nickname.text = player.nickname
            email = ET.SubElement(local_player, "email")
            email.text = player.email
            date_of_birth = ET.SubElement(local_player, "date_of_birth")
            date_of_birth.text = player.date_of_birth.strftime("%Y-%m-%d")
            xp = ET.SubElement(local_player, "xp")
            xp.text = str(player.xp)
            cls = ET.SubElement(local_player, "class")
            cls.text = player.cls

        return ET.tostring(data, encoding="unicode", method="xml")
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        pass

    def from_protobuf(self, binary):
        players_list = player_protobf.PlayersList()
        players_list.ParseFromString(binary)
        players = []

        for item in players_list.player:
            player = Player(
                item.nickname,
                item.email,
                item.date_of_birth,
                item.xp,
                player_protobf.Class.Name(item.cls)
            )
            players.append(player)

        return players
        '''
            This function should transform a binary protobuf string into a list with Player objects.
        '''
        pass

    def to_protobuf(self, list_of_players):
        player_elem = player_protobf.PlayersList()

        for item in list_of_players:
            local_player = player_elem.player.add()
            local_player.nickname = item.nickname
            local_player.email = item.email
            local_player.date_of_birth = item.date_of_birth.strftime("%Y-%m-%d")
            local_player.xp = item.xp
            local_player.cls = getattr(player_protobf.Class, item.cls)

        return player_elem.SerializeToString()
        '''
            This function should transform a list with Player objects intoa binary protobuf string.
        '''
        pass
