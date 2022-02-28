// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 实时转码子开关配置
 */
public class VideoPreviewLiveTranscodingEnableConfig extends TeaModel {
    @NameInMap("drop_file_created_event")
    public Boolean dropFileCreatedEvent;

    @NameInMap("enable_dump_old_m3u8_task_info")
    public Boolean enableDumpOldM3u8TaskInfo;

    @NameInMap("enable_ignore_copied_file")
    public Boolean enableIgnoreCopiedFile;

    public static VideoPreviewLiveTranscodingEnableConfig build(java.util.Map<String, ?> map) throws Exception {
        VideoPreviewLiveTranscodingEnableConfig self = new VideoPreviewLiveTranscodingEnableConfig();
        return TeaModel.build(map, self);
    }

    public VideoPreviewLiveTranscodingEnableConfig setDropFileCreatedEvent(Boolean dropFileCreatedEvent) {
        this.dropFileCreatedEvent = dropFileCreatedEvent;
        return this;
    }
    public Boolean getDropFileCreatedEvent() {
        return this.dropFileCreatedEvent;
    }

    public VideoPreviewLiveTranscodingEnableConfig setEnableDumpOldM3u8TaskInfo(Boolean enableDumpOldM3u8TaskInfo) {
        this.enableDumpOldM3u8TaskInfo = enableDumpOldM3u8TaskInfo;
        return this;
    }
    public Boolean getEnableDumpOldM3u8TaskInfo() {
        return this.enableDumpOldM3u8TaskInfo;
    }

    public VideoPreviewLiveTranscodingEnableConfig setEnableIgnoreCopiedFile(Boolean enableIgnoreCopiedFile) {
        this.enableIgnoreCopiedFile = enableIgnoreCopiedFile;
        return this;
    }
    public Boolean getEnableIgnoreCopiedFile() {
        return this.enableIgnoreCopiedFile;
    }

}
