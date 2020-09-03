// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 列举uploadID对应的已上传分片
     */
    public class ListUploadedPartRequest : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string FileId { get; set; }

        /// <summary>
        /// limit
        /// </summary>
        [NameInMap("limit")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public long Limit { get; set; }

        /// <summary>
        /// part_number_marker
        /// </summary>
        [NameInMap("part_number_marker")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public long PartNumberMarker { get; set; }

        /// <summary>
        /// upload_id
        /// </summary>
        [NameInMap("upload_id")]
        [Validation(Required=false)]
        public string UploadId { get; set; }

    }

}
