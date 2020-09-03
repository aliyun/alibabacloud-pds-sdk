// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 搜索文件元数据
     */
    public class SearchFileRequest : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// image_thumbnail_process
        /// </summary>
        [NameInMap("image_thumbnail_process")]
        [Validation(Required=false)]
        public string ImageThumbnailProcess { get; set; }

        /// <summary>
        /// image_url_process
        /// </summary>
        [NameInMap("image_url_process")]
        [Validation(Required=false)]
        public string ImageUrlProcess { get; set; }

        /// <summary>
        /// limit
        /// </summary>
        [NameInMap("limit")]
        [Validation(Required=false)]
        public int? Limit { get; set; }

        /// <summary>
        /// Marker
        /// </summary>
        [NameInMap("marker")]
        [Validation(Required=false)]
        public string Marker { get; set; }

        /// <summary>
        /// order_by
        /// </summary>
        [NameInMap("order_by")]
        [Validation(Required=false)]
        public string OrderBy { get; set; }

        /// <summary>
        /// query
        /// </summary>
        [NameInMap("query")]
        [Validation(Required=false, MaxLength=4096)]
        public string Query { get; set; }

        /// <summary>
        /// url_expire_sec
        /// </summary>
        [NameInMap("url_expire_sec")]
        [Validation(Required=false)]
        public long UrlExpireSec { get; set; }

        /// <summary>
        /// video_thumbnail_process
        /// type:string
        /// </summary>
        [NameInMap("video_thumbnail_process")]
        [Validation(Required=false)]
        public string VideoThumbnailProcess { get; set; }

    }

}
