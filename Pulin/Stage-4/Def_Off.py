class demo:
    two_x_mode_check=False

    def check_2_x_winning_condition(self, basket_stacks):
        cnt = 0
        for i, basket in enumerate(basket_stacks):
            if basket == ['1','1','1'] or  basket == ['1','0','1'] or basket == ['0','1','1']:
                cnt += 1
        if cnt == 2:
            return True
        else:
            return False


    def evaluate_priority(self, basket):
        if self.two_x_mode_check:
            if basket == ['', '', '']:
                return 3
            elif basket == ['0', '', '']:
                return 2
            elif basket == ['1', '', '']:
                return 1
            elif basket == ['0', '1', '']:
                return 7
            elif basket == ['0', '0', '']:
                return 4
            elif basket == ['1', '0', '']:
                return 6
            elif basket == ['1', '1', '']:
                return 5
            else:
                return 0  # Def_for_2_x
        else:
            if basket == ['', '', '']:
                return 3
            elif basket == ['0', '', '']:
                return 2
            elif basket == ['1', '', '']:
                return 1
            elif basket == ['0', '1', '']:
                return 7
            elif basket == ['0', '0', '']:
                return 5
            elif basket == ['1', '0', '']:
                return 6
            elif basket == ['1', '1', '']:
                return 4
            else:
                return 0  # Off


    def apply_move(self, basket_stack):
        for i, ball in enumerate(basket_stack):
            if ball == '':
                basket_stack[i] = '0'
                return basket_stack


    def select_move(self, basket_stacks):
        max_priority = 0
        selected_move = None

        for i, basket in enumerate(basket_stacks):
            priority = self.evaluate_priority(basket)
            if priority > max_priority:
                max_priority = priority
                selected_move = i
        return selected_move

    def main(self,basket_stacks):
        
        two_x_mode_check = self.check_2_x_winning_condition(basket_stacks)

        selected_move = self.select_move(basket_stacks)
        # print("Silo Selected By Blue Team : ",selected_move)

        self.apply_move(basket_stacks[selected_move])

        # print("Next state of basket stacks:", basket_stacks)

        return basket_stacks