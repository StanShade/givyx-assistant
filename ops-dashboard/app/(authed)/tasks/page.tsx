import { TasksBoard } from "@/components/TasksBoard.tsx";
import { readTasks } from "@/lib/store.ts";
import { taskViews } from "@/lib/tasks.ts";

export const dynamic = "force-dynamic";
export const metadata = { title: "Tasks — Givyx Ops" };

export default async function TasksPage() {
  const { doc } = await readTasks();
  return <TasksBoard initial={taskViews(doc)} />;
}
