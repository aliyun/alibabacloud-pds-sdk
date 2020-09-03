// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 文件移动请求
     */
    public class MoveFileRequest : TeaModel {
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
        /// new_name
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false, MaxLength=1024)]
        public string NewName { get; set; }

        /// <summary>
        /// overwrite
        /// type: boolean
        /// </summary>
        [NameInMap("overwrite")]
        [Validation(Required=false)]
        public bool? Overwrite { get; set; }

        /// <summary>
        /// to_parent_file_id
        /// </summary>
        [NameInMap("to_parent_file_id")]
        [Validation(Required=true, MaxLength=50)]
        public string ToParentFileId { get; set; }

    }

}
