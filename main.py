class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, category="عام"):
        new_task = {
            "id": len(self.tasks) + 1,
            "task": task,
            "category": category,
            "completed": False
        }
        self.tasks.append(new_task)
        return f"تمت إضافة المهمة: {task}"
    
    def show_tasks(self):
        if not self.tasks:
            return "لا توجد مهام حالياً"
        
        result = "\n" + "="*40 + "\n"
        result += "قائمة المهام:\n"
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            result += f"{task['id']}. [{status}] {task['task']} - {task['category']}\n"
        result += "="*40
        return result

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return f"تم إكمال المهمة: {task['task']}"
        return "لم يتم العثور على المهمة"

# مثال للاستخدام
if __name__ == "__main__":
    manager = TaskManager()
    print(manager.add_task("تعلم Git و GitHub", "تعلم"))
    print(manager.add_task("إنشاء مشروع للمقابلة", "عمل"))
    print(manager.show_tasks())
