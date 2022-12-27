// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 获取文件夹size信息
 */
public class GetDirSizeInfoResponse extends TeaModel {
    /**
     * <p>dir_count</p>
     */
    @NameInMap("dir_count")
    public Long dirCount;

    /**
     * <p>file_count</p>
     */
    @NameInMap("file_count")
    public Long fileCount;

    /**
     * <p>size</p>
     */
    @NameInMap("size")
    public Long size;

    public static GetDirSizeInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        GetDirSizeInfoResponse self = new GetDirSizeInfoResponse();
        return TeaModel.build(map, self);
    }

    public GetDirSizeInfoResponse setDirCount(Long dirCount) {
        this.dirCount = dirCount;
        return this;
    }
    public Long getDirCount() {
        return this.dirCount;
    }

    public GetDirSizeInfoResponse setFileCount(Long fileCount) {
        this.fileCount = fileCount;
        return this;
    }
    public Long getFileCount() {
        return this.fileCount;
    }

    public GetDirSizeInfoResponse setSize(Long size) {
        this.size = size;
        return this;
    }
    public Long getSize() {
        return this.size;
    }

}
