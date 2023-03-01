// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class SimilarImageCluster extends TeaModel {
    @NameInMap("files")
    public java.util.List<BaseCCPFileResponse> files;

    public static SimilarImageCluster build(java.util.Map<String, ?> map) throws Exception {
        SimilarImageCluster self = new SimilarImageCluster();
        return TeaModel.build(map, self);
    }

    public SimilarImageCluster setFiles(java.util.List<BaseCCPFileResponse> files) {
        this.files = files;
        return this;
    }
    public java.util.List<BaseCCPFileResponse> getFiles() {
        return this.files;
    }

}
