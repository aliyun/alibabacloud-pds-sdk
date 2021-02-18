<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 批量删除文件请求
 */
class DeleteFilesRequest extends Model {
    protected $_name = [
        'driveId' => 'drive_id',
        'fileIdList' => 'file_id_list',
        'shareId' => 'share_id',
    ];
    public function validate() {
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateRequired('fileIdList', $this->fileIdList, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileIdList) {
            $res['file_id_list'] = $this->fileIdList;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return DeleteFilesRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['drive_id'])){
            $model->driveId = $map['drive_id'];
        }
        if(isset($map['file_id_list'])){
            if(!empty($map['file_id_list'])){
                $model->fileIdList = $map['file_id_list'];
            }
        }
        if(isset($map['share_id'])){
            $model->shareId = $map['share_id'];
        }
        return $model;
    }
    /**
     * @description drive_id
     * @example 1
     * @var string
     */
    public $driveId;

    /**
     * @description file_id_list
     * @example 
     * @var string[]
     */
    public $fileIdList;

    /**
     * @description share_id
     * @var string
     */
    public $shareId;

}
