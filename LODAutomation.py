import unreal

PML = unreal.ProceduralMeshLibrary
ELL = unreal.EditorUtilityLibrary

def Lod_Automation():
    staticMeshes = ELL.get_selected_assets()
    bound = ELL.get_selection_bounds()
    viewport_selection = ELL.get_selection_set()
    
    for staticMesh in staticMeshes:
        #bound[2] = staticMesh.get_bound[2]s().sphere_radius 
        numLODs = staticMesh.get_num_lods()
        for i in range(numLODs):
            numSections = staticMesh.get_num_sections(i)

            for j in range(numSections):
                sectionData = PML.get_section_from_static_mesh(staticMesh, i, j)
                triangle_count = len(sectionData[1]) / 3
                print(round(triangle_count))
                print(round(bound[2]))

                # HighTriangleCountForLargeMesh
                if triangle_count > 10000 and bound[2] > 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.6, 0.6),
                        unreal.EditorScriptingMeshReductionSettings(0.35, 0.45),
                        unreal.EditorScriptingMeshReductionSettings(0.15, 0.35)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # HighTriangleCountForMediumMesh
                elif triangle_count > 10000 and bound[2] > 50 and bound[2] < 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.6, 0.25),
                        unreal.EditorScriptingMeshReductionSettings(0.35, 0.15),
                        unreal.EditorScriptingMeshReductionSettings(0.15, 0.075)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # HighTriangleCountForSmallMesh
                elif triangle_count > 10000 and bound[2] < 50:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.6, 0.1),
                        unreal.EditorScriptingMeshReductionSettings(0.35, 0.075),
                        unreal.EditorScriptingMeshReductionSettings(0.15, 0.045)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # MediumTriangleCountForLargeMesh
                elif triangle_count > 1000 and triangle_count < 10000 and bound[2] > 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.75, 0.6),
                        unreal.EditorScriptingMeshReductionSettings(0.5, 0.45),
                        unreal.EditorScriptingMeshReductionSettings(0.25, 0.35)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # MediumTriangleCountForMediumMesh
                elif triangle_count > 1000 and triangle_count < 10000 and bound[2] > 50 and bound[2] < 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.6, 0.25),
                        unreal.EditorScriptingMeshReductionSettings(0.3, 0.15),
                        unreal.EditorScriptingMeshReductionSettings(0.15, 0.075)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # MediumTriangleCountForSmallMesh
                elif triangle_count > 1000 and triangle_count < 10000 and bound[2] < 50:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.6, 0.1),
                        unreal.EditorScriptingMeshReductionSettings(0.3, 0.075),
                        unreal.EditorScriptingMeshReductionSettings(0.15, 0.045)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # LowTriangleCountForLargeMesh
                elif triangle_count < 1000 and bound[2] > 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.8, 0.6),
                        unreal.EditorScriptingMeshReductionSettings(0.7, 0.45),
                        unreal.EditorScriptingMeshReductionSettings(0.5, 0.35)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # LowTriangleCountForMediumMesh
                elif triangle_count < 1000 and bound[2] > 50 and bound[2] < 200:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.8, 0.25),
                        unreal.EditorScriptingMeshReductionSettings(0.7, 0.15),
                        unreal.EditorScriptingMeshReductionSettings(0.5, 0.075)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

                # LowTriangleCountForSmallMesh
                elif triangle_count < 1000 and bound[2] < 50:
                    reduction_options = unreal.EditorScriptingMeshReductionOptions()
                    reduction_options.reduction_settings = [
                        unreal.EditorScriptingMeshReductionSettings(1.0, 1.0),
                        unreal.EditorScriptingMeshReductionSettings(0.8, 0.1),
                        unreal.EditorScriptingMeshReductionSettings(0.7, 0.075),
                        unreal.EditorScriptingMeshReductionSettings(0.5, 0.045)
                    ]
                    reduction_options.auto_compute_lod_screen_size = False
                    unreal.EditorStaticMeshLibrary.set_lods(staticMesh, reduction_options)

Lod_Automation()