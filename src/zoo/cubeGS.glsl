// Some text replacements disabled with leading hyphen
//VTK::System::Dec
//-VTK::PositionVC::Dec

//VTK::CustomUniforms::Dec

in vec4 vertexColorVSOutput[];
out vec4 vertexColorGSOutput;
in vec4 vertexVCVSOutput[];
in vec4 vertexMCVSOutput[];

in vec4 dispMCVSOutput[];
in float scalarVSOutput[];
in float maskscalarVSOutput[];

out vec4 vertexVCGSOutput;
out vec3 normalVCGSOutput;

uniform mat4 MCDCMatrix;
uniform mat4 MCVCMatrix;

//VTK::PrimID::Dec
//-VTK::Color::Dec
//-VTK::Normal::Dec
//VTK::Light::Dec
//VTK::TCoord::Dec
//VTK::Picking::Dec
//VTK::DepthPeeling::Dec
//VTK::Clip::Dec
//VTK::Output::Dec

layout(points) in;
layout(triangle_strip, max_vertices = 24) out;

uniform vec4 cube_strip[] = {
    // front
    vec4(-1.f,  1.f,  1.f, 0.f),
    vec4(-1.f, -1.f,  1.f, 0.f),
    vec4( 1.f,  1.f,  1.f, 0.f),
    vec4( 1.f, -1.f,  1.f, 0.f),
    // right
    vec4( 1.f,  1.f,  1.f, 0.f),
    vec4( 1.f, -1.f,  1.f, 0.f),
    vec4( 1.f,  1.f, -1.f, 0.f),
    vec4( 1.f, -1.f, -1.f, 0.f),
    // back
    vec4( 1.f,  1.f, -1.f, 0.f),
    vec4( 1.f, -1.f, -1.f, 0.f),
    vec4(-1.f,  1.f, -1.f, 0.f),
    vec4(-1.f, -1.f, -1.f, 0.f),
    // left
    vec4(-1.f,  1.f, -1.f, 0.f),
    vec4(-1.f, -1.f, -1.f, 0.f),
    vec4(-1.f,  1.f,  1.f, 0.f),
    vec4(-1.f, -1.f,  1.f, 0.f),
    // top
    vec4( 1.f,  1.f,  1.f, 0.f),
    vec4( 1.f,  1.f, -1.f, 0.f),
    vec4(-1.f,  1.f,  1.f, 0.f),
    vec4(-1.f,  1.f, -1.f, 0.f),
    // bottom
    vec4(-1.f, -1.f,  1.f, 0.f),
    vec4(-1.f, -1.f, -1.f, 0.f),
    vec4( 1.f, -1.f,  1.f, 0.f),
    vec4( 1.f, -1.f, -1.f, 0.f)
};

uniform vec3 face_normals[] = {
    vec3( 0.0,  0.0,  1.0), // front
    vec3( 1.0,  0.0,  0.0), // right
    vec3( 0.0,  0.0, -1.0), // back
    vec3(-1.0,  0.0,  0.0), // left
    vec3( 0.0,  1.0,  0.0), // top
    vec3( 0.0, -1.0,  0.0)  // bottom
};

float insideBox3D(vec4 v, vec3 bottomLeft, vec3 topRight) {
    vec3 s = step(bottomLeft.xyz, v.xyz) - step(topRight.xyz, v.xyz);
    return s.x * s.y * s.z;
}

void main()
{
    vertexColorGSOutput = vertexColorVSOutput[0];

    vec4 center = gl_in[0].gl_Position; // i.e. vertexDCVSOutput - display coordinates

    if (maskscalarVSOutput[0] < mask_limits[0] || maskscalarVSOutput[0] > mask_limits[1]) {
        vertexColorGSOutput.a = mask_opacity;
        // vertexColorGSOutput = vec4(255,0.0,0.0,1.0);
        // return;
    }
    if (insideBox3D(vertexMCVSOutput[0], bottomLeft-epsilon_vector, topRight+epsilon_vector) == 0.0) {
        vertexColorGSOutput.a = clip_opacity;
        // vertexColorGSOutput = vec4(255,0.0,0.0,1.0);
        // return;
    }

    for (int i = 0; i<24; i++) {
        gl_Position = center + MCDCMatrix * ((
            dispMCVSOutput[0] * disp_scale + cube_strip[i] * glyph_scale/2
        )/modelSize);
        vertexVCGSOutput = vertexVCVSOutput[0] + MCVCMatrix * ((
            dispMCVSOutput[0] * disp_scale + cube_strip[i] * glyph_scale/2
        )/modelSize);
        normalVCGSOutput = mat3(MCVCMatrix) * face_normals[i/(24/6)];
        EmitVertex();

        if ((i+1)%4 == 0) {
            EndPrimitive();
        }
    }
}
