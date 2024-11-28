class GlobalVarMonitor:
    def __init__(self):
        self.call_count = 0
        self.global_vars = {}

    def __call__(self):
        self.call_count += 1
        var_name = f'global_var_{self.call_count}'
        self.global_vars[var_name] = False  # 初始化为 False
        print(f'创建全局变量: {var_name}，当前调用次数: {self.call_count}')
        return var_name

    def set_var(self, var_name, value):
        if var_name in self.global_vars:
            self.global_vars[var_name] = value
            print(f'更新 {var_name} 为 {value}')
        else:
            print(f'错误: {var_name} 不存在')

    def get_var(self, var_name):
        return self.global_vars.get(var_name, None)

    def monitor_changes(self):
        for var_name, value in self.global_vars.items():
            print(f'{var_name} 当前值: {value}')
