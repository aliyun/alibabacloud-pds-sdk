// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 人脸分组数组
 */
public class ImageFaceGroupsResponse extends TeaModel {
    @NameInMap("face_groups")
    public java.util.List<ImageFaceGroupResponse> faceGroups;

    public static ImageFaceGroupsResponse build(java.util.Map<String, ?> map) throws Exception {
        ImageFaceGroupsResponse self = new ImageFaceGroupsResponse();
        return TeaModel.build(map, self);
    }

    public ImageFaceGroupsResponse setFaceGroups(java.util.List<ImageFaceGroupResponse> faceGroups) {
        this.faceGroups = faceGroups;
        return this;
    }
    public java.util.List<ImageFaceGroupResponse> getFaceGroups() {
        return this.faceGroups;
    }

}
