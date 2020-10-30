<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Remove story images request.
 */
class RemoveStoryImagesRequest extends Model
{
    /**
     * @var string
     */
    public $driveId;

    /**
     * @var string[]
     */
    public $fileIds;

    /**
     * @var string
     */
    public $storyId;
    protected $_name = [
        'driveId' => 'drive_id',
        'fileIds' => 'file_ids',
        'storyId' => 'story_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->fileIds) {
            $res['file_ids'] = $this->fileIds;
        }
        if (null !== $this->storyId) {
            $res['story_id'] = $this->storyId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return RemoveStoryImagesRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['file_ids'])) {
            if (!empty($map['file_ids'])) {
                $model->fileIds = $map['file_ids'];
            }
        }
        if (isset($map['story_id'])) {
            $model->storyId = $map['story_id'];
        }

        return $model;
    }
}
