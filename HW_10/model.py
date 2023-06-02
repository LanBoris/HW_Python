class TablePlayers:
    
    def __init__(self, path: str = 'table.txt'):
        self._table_players: list[dict[str, str]] =[]
        self._path = path
        self._last_id = 0

    def open_table_players(self):
        with open(self._path, 'r', encoding = 'utf-8') as file:
            data = file.readlines()
        for player in data:
            player = player.strip().split(':')
            new = {'id': player[0], 'name':player[1], 'score':player[2]}
            self._table_players.append(new)

    def show_table_players(self):
        return self._table_players

    def add_player(self, new: dict[str, str]) -> str:
        new_id = self._last_id + 1
        new['id'] = str(new_id)
        new_score = 0
        new['score'] = str(new_score)
        self._table_players.append(new)
        return new.get('name')

    def save_table_players(self):
        data = []
        for player in self._table_players:
            data.append(':'.join([player['id'], player['name'], player['score']]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding = 'utf-8') as file:
            file.write(data)

    def count_points(self, name: str, new_score: int):
        for player in self._table_players:
            if player.get('name').lower() == name.lower():
                player['score'] = str(int(player.get('score')) + new_score)
        

