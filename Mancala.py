# Author: Hope Schenck
# GitHub username: schenckus
# Date: 12/3/2022
# Description: A program that has one Class called Mancala. It simulates the real life game through
#             functions that initialize the two players, the ability to print the board, returns the
#             winners and has a function for the players to play the game.


class Mancala:
    """
    A class that allows two players to play a web-version of the game named Mancala. Includes methods
    to create two players, prints the board, returns winner, and play the game.
    """

    def __init__(self):
        self._player_1 = None
        self._player_2 = None
        self._player_1_store = 0
        self._player_2_store = 0
        self._player_1_pod_list = [4, 4, 4, 4, 4, 4]
        self._player_2_pod_list = [4, 4, 4, 4, 4, 4]

    def create_player(self, players_name):
        """
        :param players_name: a string for each player's name
        :return: creates two players for the Mancala game. If more players
        attempt to be created, raises OnlyTwoPlayersError
        """
        # if player 1 is empty, create player 1
        if self._player_1 is None:
            self._player_1 = players_name
            return self._player_1

        # if player 1 is filled, and player 2 is empty, create player 2
        if self._player_1 is not None:
            if self._player_2 is None:
                self._player_2 = players_name
                return self._player_2

        if self._player_1 and self._player_2 is not None:
            raise OnlyTwoPlayersError

    def get_player_1(self):
        """
        :return: the object location of player 1
        """
        return self._player_1

    def get_player_2(self):
        """
        :return: the object location of player 2
        """
        return self._player_2

    def print_board(self):
        """
        :return: prints players 1 and 2's store amount and pods.
        """
        # initialize player 1 and 2 using get methods
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # grabs player 1's store amount and pod
        store1 = self.get_store_amount(player1)
        pod1 = self.get_player_pod(player1)

        # prints player 1's store amount and board
        print("player1:")
        print("store: " + str(store1))
        print(pod1)

        # grabs player 2's store amount and board
        store2 = self.get_store_amount(player2)
        pod2 = self.get_player_pod(player2)

        # prints player 2's store amount and board
        print("player2:")
        print("store: " + str(store2))
        print(pod2)

    def return_winner(self):
        """
        :return: if player 1 or 2's pits are empty, then the person with the most seeds in their store wins regardless
        of who empties their pods first.
        """
        # initialize player 1 and 2 using get methods
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # initialize player 1 and 2 pods
        pod1 = self.get_player_pod(player1)
        pod2 = self.get_player_pod(player2)

        # if players 1's pods are completely empty.
        if pod1 == [0, 0, 0, 0, 0, 0]:
            # grab player 2's seeds and put it into player 2's store
            index = 0
            # iterate over player 2's pods
            while index < 6:
                seeds = pod2[index]
                # add seeds to store
                self.add_to_store(player2, seeds)
                # move to next position
                pod2[index] = 0
                index += 1

        # if players 2's pods are completely empty.
        if pod2 == [0, 0, 0, 0, 0, 0]:
            # grab player 1's seeds and put it into player 1's store
            index = 0
            # iterate over player 1's pods
            while index < 6:
                seeds = pod1[index]
                # add seeds to store
                self.add_to_store(player1, seeds)
                # move to next position
                pod1[index] = 0
                index += 1

        # if no one has won yet
        else:
            return "Game has not ended"

        # whoever has more seeds in their store wins!
        store1 = self.get_store_amount(player1)
        store2 = self.get_store_amount(player2)

        if store1 > store2:
            return "Winner is player 1: " + player1
        if store1 < store2:
            return "Winner is player 2: " + player2
        if store1 == store2:
            return "It's a tie!"

    def play_game(self, player_index, pit_index):
        """
        :param player_index: 1 or 2
        :param pit_index: 1 through 6
        :return: this function is what enables the players to play the game. It has several nested while and if loops
        for specific wins, which are detailed below. Returns a list of the board game via a list after a player has taken a turn.
        """
        # initialize player 1 and 2
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # initialize player 1 and 2 pods
        pod1 = self.get_player_pod(player1)
        pod2 = self.get_player_pod(player2)

        # initializes player 1 and 2 store amount
        store1 = self.get_store_amount(player1)
        store2 = self.get_store_amount(player2)

        # the index of a list automatically starts at 0, so this pushes back the index by 1
        pit_index = pit_index - 1

        # return statement if pit index is out of bounds
        if pit_index > 6 or pit_index < 0:
            return "Invalid number for pit Index"

        """
        Checks both pods to make sure they are not empty
        """
        # if players 1's pods are completely empty.
        if pod1 == [0, 0, 0, 0, 0, 0]:
            # grab player 2's seeds and put it into player 2's store
            index = 0
            # iterate over player 2's pods
            while index < 6:
                seeds = pod2[index]
                # add seeds to store
                self.add_to_store(player2, seeds)
                # move to next position
                pod2[index] = 0
                index += 1

        # if players 2's pods are completely empty.
        if pod2 == [0, 0, 0, 0, 0, 0]:
            # grab player 1's seeds and put it into player 1's store
            index = 0
            # iterate over player 1's pods
            while index < 6:
                seeds = pod1[index]
                # add seeds to store
                self.add_to_store(player1, seeds)
                # move to next position
                pod1[index] = 0
                index += 1

        """
        PLAYER 1 MOVES
        """
        if player_index == 1:
            # pos equals what position of the pods player is in
            seeds = pod1[pit_index]
            # if there are no seeds in this position, return error
            if seeds == 0:
                raise NoSeedsError
            else:
                # empty current position
                pod1[pit_index] = 0

            while seeds > 0:
                """
                Special case: if player 1 lands on an empty pod on their own side
                """
                if seeds == 1 and pod1[pit_index] == 0:
                    # decrement seeds
                    seeds -= 1
                    # player 2's position
                    current_pos = (4 - pit_index)
                    # add 1 to opposite side
                    pod2[current_pos] += 1
                    # assign value to current seeds
                    seeds_from_player2 = pod2[current_pos]
                    # empty player 2's pod
                    pod2[current_pos] = 0
                    # add to player 1's store
                    self.add_to_store(player1, seeds_from_player2)

                    board_list = []

                    board_list.extend(pod1)
                    board_list.append(store1)
                    board_list.extend(pod2)
                    board_list.append(store2)
                    return board_list


                """
                if player 1 has reached their store
                """
                if pit_index >= 5:
                    """
                    Special case: player 1 gets to take another turn 
                    """
                    if pit_index >= 5 and seeds == 1:
                        # decrement the amount of seeds the player has
                        seeds -= 1
                        # add 1 seed to players store
                        self.add_to_store(player1, 1)
                        return "Player 1 take another turn"
                    else:
                        # decrement the amount of seeds the player has
                        seeds -= 1
                        # add 1 seed to players store
                        self.add_to_store(player1, 1)
                        """
                        Start going through player 2's pods 
                        """
                        pos = 0
                        pos2 = 0
                        while seeds > 0:
                            # checks to see whether pod1 is empty
                            if pod1 == [0, 0, 0, 0, 0, 0]:
                                seeds -= 1
                                # if the pods become completely empty, put the rest of the seeds in the store
                                self.add_to_store(player1, seeds)
                                # set seeds equal to 0
                                seeds = 0

                            # if you reach the end of player 2's, go back through to player 1
                            if pos >= 5:
                                if pos >= 5 and seeds == 1:
                                    # decrement the amount of seeds the player has
                                    seeds -= 1
                                    # add 1 seed to players store
                                    self.add_to_store(player1, 1)
                                    return "Player 1 take another turn"
                                else:
                                    # add 1 seed to players store
                                    self.add_to_store(player1, 1)
                                    pod2[pos2] += 1
                                    seeds -= 1
                                    pos2 += 1
                            # else, continue through player 2's pods
                            else:
                                # add 1 seed to player's two board
                                pod2[pos] += 1
                                # decrement seeds
                                seeds -= 1
                                # decrement position on player two boards
                                pos += 1

                else:
                    # move to next pod
                    pit_index += 1
                    # decrement the amount of seeds the player has
                    seeds -= 1
                    # drop 1 into next position
                    pod1[pit_index] += 1

        """
        PLAYER 2 MOVES
        """
        if player_index == 2:
            # pos equals what position of the pods player is in
            seeds = pod2[pit_index]
            # if there are no seeds in this position, return error
            if seeds == 0:
                return NoSeedsError
            else:
                # empty current position
                pod2[pit_index] = 0

            while seeds > 0:

                """
                Special case: if player 2 lands on an empty pod on their own side
                """
                if seeds == 1 and pod2[pit_index] == 0:
                    # decrement seeds
                    seeds -= 1
                    # add 1 to opposite side
                    pod1[pit_index] += 1
                    # assign value to current seeds
                    seeds_from_player1 = pod1[pit_index]
                    # empty player 2's pod
                    pod1[pit_index] = 0
                    # add to player 1's store
                    self.add_to_store(player2, seeds_from_player1)

                    board_list = []

                    board_list.extend(pod1)
                    board_list.append(store1)
                    board_list.extend(pod2)
                    board_list.append(store2)
                    return board_list

                """
                If player 2 has reached their store
                """
                if pit_index >= 5:
                    """
                    Special case: player 2 gets to take another turn 
                    """
                    if pit_index >= 5 and seeds == 1:
                        # decrement the amount of seeds the player has
                        seeds -= 1
                        # add 1 seed to players store
                        self.add_to_store(player2, 1)
                        return "Player 2 take another turn"
                    else:
                        # decrement the amount of seeds the player has
                        seeds -= 1
                        # add 1 seed to players store
                        self.add_to_store(player2, 1)
                        """
                        Start going through player 1's pods 
                        """
                        pos = 0
                        pos2 = 0
                        while seeds > 0:
                            # checks to see whether pod2 is empty
                            if pod2 == [0, 0, 0, 0, 0, 0]:
                                seeds -= 1
                                # if the pods become completely empty, put the rest of the seeds in the store
                                self.add_to_store(player2, seeds)
                                # set seeds equal to 0
                                seeds = 0
                            # if you reach the end of player 1's, go back through to player 2
                            if pos >= 5:
                                if pos >= 5 and seeds == 1:
                                    # decrement the amount of seeds the player has
                                    seeds -= 1
                                    # add 1 seed to players store
                                    self.add_to_store(player2, 1)
                                    return "Player 1 take another turn"
                                else:
                                    # add 1 seed to players store
                                    self.add_to_store(player2, 1)
                                    pod1[pos2] += 1
                                    seeds -= 1
                                    pos2 += 1
                            # else, continue through player 1's pods
                            else:
                                # add 1 seed to player's two board
                                pod1[pos] += 1
                                # decrement seeds
                                seeds -= 1
                                # decrement position on player two boards
                                pos += 1
                else:
                    # move to next pod
                    pit_index += 1
                    # decrement the amount of seeds the player has
                    seeds -= 1
                    # drop 1 into next position
                    pod2[pit_index] += 1
        """
        Checks both pods to make sure they are not empty (AGAIN)
        """
        # if players 1's pods are completely empty.
        if pod1 == [0, 0, 0, 0, 0, 0]:
            # grab player 2's seeds and put it into player 2's store
            index = 0
            # iterate over player 2's pods
            while index < 6:
                seeds = pod2[index]
                # add seeds to store
                self.add_to_store(player2, seeds)
                # move to next position
                pod2[index] = 0
                index += 1

        # if players 2's pods are completely empty.
        if pod2 == [0, 0, 0, 0, 0, 0]:
            # grab player 1's seeds and put it into player 1's store
            index = 0
            # iterate over player 1's pods
            while index < 6:
                seeds = pod1[index]
                # add seeds to store
                self.add_to_store(player1, seeds)
                # move to next position
                pod1[index] = 0
                index += 1

        # board list that displays the current board
        board_list = []

        board_list.extend(pod1)
        board_list.append(store1)
        board_list.extend(pod2)
        board_list.append(store2)
        return board_list

    def get_store_amount(self, player):
        """
        :param player: either player_1 or player_2
        :return: the current amount in the players store
        """
        # initialize player 1 and 2
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # return player 1's store amount
        if player == player1:
            return self._player_1_store

        # return player 2's store amount
        if player == player2:
            return self._player_2_store

    def add_to_store(self, player, amount):
        """
        :param player: either player_1 or player_2
        :param amount: how many seeds to add to store
        :return: how many seeds the player has
        """
        # initialize player 1 and 2
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # add amount to player 1's store
        if player == player1:
            self._player_1_store += amount
            return amount

        # add amount to player 2's store
        if player == player2:
            self._player_2_store += amount
            return amount

    def get_player_pod(self, player):
        """
        :param player:
        :return: either player 1 or 2's board, doesn't include Store
        """
        # initialize player 1 and 2
        player1 = self.get_player_1()
        player2 = self.get_player_2()

        # returns player 1's pods and seeds
        if player == player1:
            return self._player_1_pod_list

        # returns player 2's pods and seeds
        if player == player2:
            return self._player_2_pod_list


class NoSeedsError(Exception):
    pass


class OnlyTwoPlayersError(Exception):
    pass

