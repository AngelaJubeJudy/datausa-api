# registrar.py
from datausa.core import get_columns
from datausa.core.registrar import registered_models

class TableManager(object):
    possible_variables = [col.key for t in registered_models for col in get_columns(t)]

    @classmethod
    def table_can_show(cls, table, shows_and_levels):
        for show_col, show_level in shows_and_levels.items():
            if not show_col in table.supported_levels:
                return False
            else:
                print table.supported_levels[show_col]
                if not show_level in table.supported_levels[show_col]:
                    return False
        return True
    
    @classmethod
    def table_has_cols(cls, table, vars_needed):
        cols = set([col.name for col in get_columns(table)])
        # if table.__tablename__ == 'grads_yucd':
            # raise Exception("t")
        return set(vars_needed).issubset(cols)

    @classmethod
    def find_table(cls, vars_needed, shows_and_levels):
        for table in registered_models:
            if TableManager.table_has_cols(table, vars_needed):
                if TableManager.table_can_show(table, shows_and_levels):
                    return table
        raise DataUSAException("No tables can match the specified query.")
