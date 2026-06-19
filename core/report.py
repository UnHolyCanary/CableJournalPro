class ProjectReport:

    @staticmethod
    def create(project):

        lines = []

        lines.append("DXF INSPECTOR")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Файл................ {project.name}")
        lines.append(f"Версия DXF.......... {project.version}")
        lines.append(f"Количество слоев.... {len(project.layers)}")
        lines.append(f"Количество блоков... {project.blocks}")
        lines.append(f"Количество объектов. {project.entities}")

        lines.append("")
        lines.append("=" * 60)
        lines.append("Типы объектов")
        lines.append("")

        lines.append("")
        lines.append("=" * 60)
        lines.append("Блоки проекта")
        lines.append("")

        for block, count in project.block_info.items():
            lines.append(f"{block:<40}{count}")

        for entity, count in sorted(project.types.items()):
            lines.append(f"{entity:<20}{count}")

        lines.append("")
        lines.append("=" * 60)
        lines.append("Слои проекта")
        lines.append("")

        for layer, count in project.layer_info.items():
            lines.append(f"{layer:<35}{count}")

        return "\n".join(lines)
