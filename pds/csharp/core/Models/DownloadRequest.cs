// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 下载文件请求body
     */
    public class DownloadRequest : TeaModel {
        /// <summary>
        /// drive id
        /// </summary>
        [NameInMap("DriveID")]
        [Validation(Required=false)]
        public string DriveID { get; set; }

        /// <summary>
        /// file id
        /// </summary>
        [NameInMap("FileID")]
        [Validation(Required=true)]
        public string FileID { get; set; }

        /// <summary>
        /// in: query
        /// image_thumbnail_process
        /// </summary>
        [NameInMap("ImageThumbnailProcess")]
        [Validation(Required=false)]
        public string ImageThumbnailProcess { get; set; }

        /// <summary>
        /// share_id, either share_id or drive_id is required
        /// </summary>
        [NameInMap("ShareID")]
        [Validation(Required=false)]
        public string ShareID { get; set; }

        /// <summary>
        /// video_thumbnail_process
        /// type:string
        /// </summary>
        [NameInMap("VideoThumbnailProcess")]
        [Validation(Required=false)]
        public string VideoThumbnailProcess { get; set; }

    }

}
